export default function MessageBubble({ role, text, references }) {
  return (
    <div className={`bubble-wrapper ${role}`}>
      <div className={`bubble ${role}`}>{text}</div>
      {references && references.length > 0 && (
        <div className="references">
          {references.map((ref, i) => (
            <a key={i} href={ref.url} target="_blank" rel="noreferrer">
              {ref.title}
            </a>
          ))}
        </div>
      )}
    </div>
  );
}
