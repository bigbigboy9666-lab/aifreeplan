export function toolSchema(tool: Record<string, any>, locale: string) {
  const lang = locale;
  const name = tool[`name_${lang}`] || tool.name_en;
  const desc = tool[`description_${lang}`] || tool.description_en;
  const catName = tool[`category_${lang}`] || tool.category_en;
  const faq = tool[`faq_${lang}`] || [];

  const schemas: Record<string, any>[] = [];

  // SoftwareApplication
  schemas.push({
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
  });

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
  schemas.push({
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: title,
    description: desc.slice(0, 200),
    image: guide.image || guide.cover_image || `https://aifreeplan.com/og-guides/${guide.slug}.png`,
    author: { '@type': 'Organization', name: 'AIFreePlan' },
    datePublished: guide.date_published,
    dateModified: guide.date_modified,
    publisher: { '@type': 'Organization', name: 'AIFreePlan', url: 'https://aifreeplan.com' },
    mainEntityOfPage: { '@type': 'WebPage', '@id': `https://aifreeplan.com/${locale}/guides/${guide.slug}` },
  });

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
