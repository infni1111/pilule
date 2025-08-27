'use client'
import { useEffect, useState } from "react";

export default function Microphone() {
  const [stream, setStream] = useState(null);

  useEffect(() => {
    async function getMicrophone() {
      try {
        // Demander la permission et obtenir le flux audio
        const userStream = await navigator.mediaDevices.getUserMedia({ audio: true });
        setStream(userStream);
        console.log("Micro activé !", userStream);
      } catch (err) {
        console.error("Erreur d'accès au micro :", err);
      }
    }

    getMicrophone();
  }, []);

  return (
    <div>
      <h1>Microphone</h1>
      {stream ? <p>Micro activé ✅</p> : <p>Demande d'accès au micro...</p>}
    </div>
  );
}
