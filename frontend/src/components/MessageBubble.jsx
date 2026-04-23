function safeUrl(url) {
  try {
    const parsed = new URL(url);
    return parsed.protocol === "https:" || parsed.protocol === "http:"
      ? parsed.href
      : null;
  } catch {
    return null;
  }
}

export default function MessageBubble({ role, text, references }) {
  return (
    <div className={`bubble-wrapper ${role}`}>
      <div className={`bubble ${role}`}>{text}</div>
      {references && references.length > 0 && (
        <div className="references">
          {references.map((ref, i) => {
            const href = safeUrl(ref.url);
            return href ? (
              <a key={i} href={href} target="_blank" rel="noopener noreferrer">
                {ref.title}
              </a>
            ) : null;
          })}
        </div>
      )}
    </div>
  );
}
