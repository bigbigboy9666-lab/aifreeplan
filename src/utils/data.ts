import toolsData from '../content/tools.json';
import guidesData from '../content/guides.json';

export function getTools() {
  return (toolsData as any[]).map((tool) => ({
    id: tool.slug,
    data: tool,
  }));
}

export function getGuides() {
  return (guidesData as any[]).map((guide) => ({
    id: guide.slug,
    data: guide,
  }));
}
