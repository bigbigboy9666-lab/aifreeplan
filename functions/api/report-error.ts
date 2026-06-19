interface Env {
  ERROR_REPORTS_KV: KVNamespace;
}

interface ErrorReport {
  toolId?: string;
  url?: string;
  errorType: string;
  description: string;
  userAgent?: string;
}

export const onRequestPost: PagesFunction<Env> = async (context) => {
  try {
    const body = await context.request.json<ErrorReport>();

    if (!body.errorType || !body.description) {
      return new Response(JSON.stringify({ error: 'Missing required fields' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const id = `err_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;

    await context.env.ERROR_REPORTS_KV.put(
      id,
      JSON.stringify({
        ...body,
        id,
        reportedAt: new Date().toISOString(),
        userAgent: context.request.headers.get('User-Agent') || 'unknown',
      }),
      { expirationTtl: 60 * 60 * 24 * 30 } // 30 days
    );

    return new Response(JSON.stringify({ message: 'Report received', id }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch {
    return new Response(JSON.stringify({ error: 'Internal server error' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};
