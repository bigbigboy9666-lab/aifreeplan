export type RefreshPeriod = 'daily' | 'weekly' | 'monthly' | 'one-time' | 'unknown';
export type Category = 'Video' | 'Image' | 'Text' | 'Audio' | 'Code' | 'LLM' | 'Chat' | 'Agent' | 'Productivity';

export interface FreeTierDetails {
  credits: number;
  creditUnit: string;
  refreshPeriod: RefreshPeriod;
  requiresCreditCard?: boolean;
  watermark: boolean;
  commercialUse: boolean;
  limitations?: string[];
  resolution?: string;
  models?: string;
  dailyLimit?: string;
}

export interface AITool {
  id: string;
  name: string;
  nameEn: string;
  category: Category;
  categoryZh: string;
  categoryEn: string;
  websiteUrl: string;
  affiliateUrl?: string;
  company: string;
  rating: number;
  freeTier: FreeTierDetails;
  description: string;
  descriptionEn: string;
  paidFrom: string;
  paidFromEn: string;
  pros: string[];
  prosEn: string[];
  cons: string[];
  consEn: string[];
  features: string[];
  featuresEn: string[];
  tips: string[];
  tipsEn: string[];
  lastVerifiedDate: string;
  seoMeta: {
    title: string;          // English title
    titleZh: string;        // Chinese title
    description: string;    // English description
    descriptionZh: string;  // Chinese description
    keywords: string[];
  };
}

export interface ComparisonPair {
  toolA: string;
  toolB: string;
  verdict: string;
  verdictEn: string;
}
