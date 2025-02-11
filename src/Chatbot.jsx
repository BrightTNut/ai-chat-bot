import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
  const [query, setQuery] = useState("");
  const [chatHistory, setChatHistory] = useState([]);

  // const sendQuery = async () => {
  //   if (!query.trim()) return;

  //   const response = await axios.post("http://localhost:8000/query/", {
  //     query,
  //   });
  //   setChatHistory([
  //     ...chatHistory,
  //     { user: query, bot: response.data.response },
  //   ]);
  //   setQuery("");
  // };

  return (
    <div className="chat-container">
      <div className="chat-history">
        {chatHistory.map((msg, index) => (
          <div key={index} className="chat-message">
            <p>
              <strong>You:</strong> {msg.user}
            </p>
            <p>
              <strong>Bot:</strong> {msg.bot}
            </p>
          </div>
        ))}
      </div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask about a product or supplier..."
      />
      <button
      //onClick={sendQuery}
      >
        Send
      </button>
    </div>
  );
};

export default Chatbot;
