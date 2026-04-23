import { useState } from "react";
import ChatWindow from "./components/ChatWindow";

export default function App() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: "Hello! Ask me anything about Intent-Driven Engineering.",
      references: [],
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  async function send() {
    const text = input.trim();
    if (!text || loading) return;
    setInput("");
    setMessages((prev) => [...prev, { role: "user", text, references: [] }]);
    setLoading(true);
    try {
      const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });
      const data = await res.json();
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: data.answer, references: data.references },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: "Something went wrong. Please try again.", references: [] },
      ]);
    } finally {
      setLoading(false);
    }
  }

  function handleKey(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send();
    }
  }

  return (
    <div className="app">
      <div className="header">
        <h1>Intent-Driven Engineering</h1>
        <p>Powered by Anthropic Claude</p>
      </div>
      <ChatWindow messages={messages} loading={loading} />
      <div className="input-row">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKey}
          placeholder="Ask about intent-driven engineering..."
          disabled={loading}
        />
        <button onClick={send} disabled={loading || !input.trim()}>
          Send
        </button>
      </div>
    </div>
  );
}
