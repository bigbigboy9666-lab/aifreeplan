export function toolSchema(tool: Record<string, any>, locale: string) {
  const lang = locale;
  const name = tool[`name_${lang}`] || tool.name_en;
  const desc = tool[`description_${lang}`] || tool.description_en;
  const catName = tool[`category_${lang}`] || tool.category_en;
  const faq = tool[`faq_${lang}`] || [];

  const schemas: Record<string, any>[] = [];

  // SoftwareApplication
  const appSchema: Record<string, any> = {
    '@context': 'https://schema.org',
    '@type': 'SoftwareApplication',
    name,
    description: desc.slice(0, 200),
    url: tool.official_url,
    applicationCategory: 'AI Tool',
    isAccessibleForFree: tool.free_credits?.type !== 'none',
    dateModified: tool.last_updated || new Date().toISOString().split('T')[0],
    offers: {
      '@type': 'Offer',
      price: '0',
      priceCurrency: 'USD',
      description: tool.free_credits?.[`amount_${lang}`] || tool.free_credits?.amount || 'Free tier',
    },
  };

  // Add image if available
  if (tool.image) {
    appSchema.image = tool.image;
  }

  // Add aggregateRating if rating exists
  if (tool.rating && tool.rating > 0) {
    appSchema.aggregateRating = {
      '@type': 'AggregateRating',
      ratingValue: tool.rating,
      bestRating: 5,
      worstRating: 1,
      ratingCount: tool.rating_count || 1,
    };
  }

  // Add operatingSystem
  appSchema.operatingSystem = 'Web';

  schemas.push(appSchema);

  // BreadcrumbList
  schemas.push({
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: lang === 'zh' ? '首页' : 'Home', item: `https://aifreeplan.com/${locale}` },
      { '@type': 'ListItem', position: 2, name: catName, item: `https://aifreeplan.com/${locale}/${tool.category}` },
      { '@type': 'ListItem', position: 3, name, item: `https://aifreeplan.com/${locale}/${tool.category}/${tool.slug}` },
    ],
  });

  // FAQPage
  if (faq.length > 0) {
    schemas.push({
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: faq.map((f: any) => ({
        '@type': 'Question',
        name: f.q,
        acceptedAnswer: { '@type': 'Answer', text: f.a },
      })),
    });
  }

  return schemas;
}

export function guideSchema(guide: Record<string, any>, locale: string) {
  const lang = locale;
  const title = guide[`title_${lang}`] || guide.title_en;
  const desc = guide[`description_${lang}`] || guide.description_en;
  const faq = guide[`faq_${lang}`] || [];

  const schemas: Record<string, any>[] = [];

  // Article
  const articleSchema: Record<string, any> = {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: title,
    description: desc.slice(0, 200),
    author: { '@type': 'Organization', name: 'AIFreePlan' },
    datePublished: guide.date_published,
    dateModified: guide.date_modified || guide.date_published,
    publisher: {
      '@type': 'Organization',
      name: 'AIFreePlan',
      url: 'https://aifreeplan.com',
      logo: { '@type': 'ImageObject', url: 'https://aifreeplan.com/og-default.png' },
    },
    mainEntityOfPage: { '@type': 'WebPage', '@id': `https://aifreeplan.com/${locale}/guides/${guide.slug}` },
  };

  // Add image if available
  if (guide.image) {
    articleSchema.image = guide.image;
  }

  schemas.push(articleSchema);

  // BreadcrumbList
  schemas.push({
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: lang === 'zh' ? '首页' : 'Home', item: `https://aifreeplan.com/${locale}` },
      { '@type': 'ListItem', position: 2, name: lang === 'zh' ? '使用攻略' : 'Guides', item: `https://aifreeplan.com/${locale}/guides` },
      { '@type': 'ListItem', position: 3, name: title, item: `https://aifreeplan.com/${locale}/guides/${guide.slug}` },
    ],
  });

  // FAQPage
  if (faq.length > 0) {
    schemas.push({
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: faq.map((f: any) => ({
        '@type': 'Question',
        name: f.q,
        acceptedAnswer: { '@type': 'Answer', text: f.a },
      })),
    });
  }

  // HowTo (conditional)
  if (guide.howto_steps && guide.howto_steps.length > 0) {
    schemas.push({
      '@context': 'https://schema.org',
      '@type': 'HowTo',
      name: guide[`howto_name_${lang}`] || title,
      description: guide[`howto_desc_${lang}`] || desc.slice(0, 200),
      step: guide.howto_steps.map((s: any) => ({
        '@type': 'HowToStep',
        name: s[`name_${lang}`] || s.name || '',
        text: s[`text_${lang}`] || s.text || '',
      })),
    });
  }

  return schemas;
}

// Organization schema for homepage
export function organizationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: 'AIFreePlan',
    url: 'https://aifreeplan.com',
    logo: 'https://aifreeplan.com/og-default.png',
    sameAs: [],
    description: 'AI工具免费额度聚合平台，帮你找到所有AI工具的免费额度。',
  };
}
