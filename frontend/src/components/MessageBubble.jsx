import Markdown from "react-markdown";

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

export default function MessageBubble({ role, text, references, usage }) {
  return (
    <div className={`bubble-wrapper ${role}`}>
      <div className={`bubble ${role}`}>
        {role === "assistant" ? (
          <div className="md"><Markdown>{text}</Markdown></div>
        ) : (
          text
        )}
      </div>
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
      {usage && (
        <div className="token-usage">
          ↑ {usage.input_tokens} in · {usage.output_tokens} out · {usage.input_tokens + usage.output_tokens} total tokens
        </div>
      )}
    </div>
  );
}
