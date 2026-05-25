export function t(data: Record<string, any>, field: string, lang: string): string {
  const key = `${field}_${lang}`;
  return data[key] ?? data[field] ?? '';
}

export function getOgLocale(locale: string): string {
  return locale === 'zh' ? 'zh_CN' : 'en_US';
}
