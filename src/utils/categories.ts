export const CATEGORIES: Record<string, { zh: string; en: string; emoji: string }> = {
  video:      { zh: '视频生成', en: 'Video Generation', emoji: '🎬' },
  image:      { zh: '图片生成', en: 'Image Generation', emoji: '🎨' },
  llm:        { zh: 'AI大模型', en: 'LLM', emoji: '🤖' },
  coding:     { zh: '编程助手', en: 'Coding Assistant', emoji: '💻' },
  'ai-assistant': { zh: 'AI助手', en: 'AI Assistant', emoji: '🧠' },
  audio:      { zh: 'AI音乐', en: 'AI Music', emoji: '🎵' },
};

export const NAV_LINKS = [
  { href_zh: '/zh', href_en: '/en', label_zh: '首页', label_en: 'Home' },
  { href_zh: '/zh/video', href_en: '/en/video', label_zh: '视频生成', label_en: 'Video' },
  { href_zh: '/zh/image', href_en: '/en/image', label_zh: '图片生成', label_en: 'Image' },
  { href_zh: '/zh/llm', href_en: '/en/llm', label_zh: 'AI大模型', label_en: 'LLM' },
  { href_zh: '/zh/coding', href_en: '/en/coding', label_zh: '编程助手', label_en: 'Coding' },
  { href_zh: '/zh/ai-assistant', href_en: '/en/ai-assistant', label_zh: 'AI助手', label_en: 'AI Assistant' },
  { href_zh: '/zh/audio', href_en: '/en/audio', label_zh: 'AI音乐', label_en: 'AI Music' },
  { href_zh: '/zh/guides', href_en: '/en/guides', label_zh: '使用攻略', label_en: 'Guides' },
];
