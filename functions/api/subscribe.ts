interface Env {
  SUBSCRIBER_KV?: KVNamespace;
}

export const onRequestPost: PagesFunction<Env> = async (context) => {
  // Graceful degradation: if the KV binding isn't provisioned on CF Pages yet,
  // the function previously threw and surfaced as a 500. Instead, return a
  // 200 with a `pending` marker so the front-end shows an honest "coming soon"
  // message rather than a broken endpoint.
  const kv = context.env.SUBSCRIBER_KV;
  if (!kv) {
    return new Response(
      JSON.stringify({ ok: true, pending: true, message: 'KV' }),
      { status: 200, headers: { 'Content-Type': 'application/json' } }
    );
  }

  try {
    const body = await context.request.json<{ email?: string }>();
    const email = body.email?.trim();

    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return new Response(JSON.stringify({ error: 'Invalid email' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const key = `sub:${email}`;
    const existing = await context.env.SUBSCRIBER_KV.get(key);

    if (existing) {
      return new Response(JSON.stringify({ message: 'Already subscribed' }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    await context.env.SUBSCRIBER_KV.put(
      key,
      JSON.stringify({
        email,
        subscribedAt: new Date().toISOString(),
        source: context.request.headers.get('Referer') || 'direct',
      })
    );

    return new Response(JSON.stringify({ message: 'Subscribed' }), {
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
