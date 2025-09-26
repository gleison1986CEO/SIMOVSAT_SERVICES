import { useEffect, useState } from 'react';
import {QRCodeCanvas} from 'qrcode.react';

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('/qrcode')
      .then(res => res.json())
      .then(data => setUsers(data));

  }, []);

  return (
    <div className="p-6 max-w-4xl mx-auto">
      
      <h1 className="text-2xl font-bold mb-4">Somatto Whastapp Financeiro</h1>
      <ul className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {users.map(user => (
          
            <h2 id="QRCODE">
              <h3>{user.qrcode}</h3>
              <QRCodeCanvas
                  value={user.qrcode}
                  title={"Somatto.org.br"}
                  size={400}
                  bgColor={"#ffffff"}
                  fgColor={"#010d1bff"}
                  level={"L"}
                  minVersion={4}
                  marginSize={1}
                  imageSettings={{
                    src: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fis1-ssl.mzstatic.com%2Fimage%2Fthumb%2FPurple221%2Fv4%2F73%2F1c%2F0f%2F731c0f79-5a6d-d952-99e6-4427dd152393%2FAppIcon-0-0-1x_U007emarketing-0-10-0-85-220.png%2F512x512bb.jpg&f=1&nofb=1&ipt=b23d1d1e886382154651238e0ff129abe88d93c1591e48ef7262ca39d514e24a",
                    x: undefined,
                    y: undefined,
                    height: 20,
                    width: 20,
                    opacity: 1,
                    excavate: true,
                  }}
                />
              </h2>

        ))}
      </ul>
    </div>
  );
}

export default App;
