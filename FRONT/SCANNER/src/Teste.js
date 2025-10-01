import React, { useEffect, useState } from "react";
import {QRCodeCanvas} from 'qrcode.react';
import axios from "axios";


const App = () => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Make GET request to fetch data
        axios
            .get("http://api.atise.com.br/qrcode")
            .then((response) => {
                setData(response.data);
                setLoading(false);
            })
            .catch((err) => {
                setError(err.message);
                setLoading(false);
            });
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;
  return (
    <div className="p-6 max-w-4xl mx-auto" id="BODY">
      <h1 className="text-2xl font-bold mb-4" id="SOMATTO">Somatto Financeiro</h1>
      <div id="GENERATOR">
      <ul className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {data.map(post => (
            
            <h2>
              <div id="QRCODE">
              <center><QRCodeCanvas
                  value={post.qrcode}
                  title={"Somatto.org.br"}
                  size={300}
                  bgColor={"#ffffff"}
                  fgColor={"#010d1bff"}
                  level={"L"}
                  minVersion={4}
                  marginSize={1}
                /></center>
              </div>  
              <div id="CODE">
              <h3>{post.qrcode}</h3>
              <span>  {post.qrcode === "Verificado" ? (
                  <button id="GREEN"><span>*Whatsapp Verfiicado com Sucesso!</span></button>
                ) : (
                  <button id="RED" onClick={() =>  navigator.clipboard.writeText(post.qrcode)}> Copiar Qrcode</button> 
                   
                )}
              
              </span> 
                           
              </div>                
              </h2>

        ))}
      </ul>
      </div>
    </div>
  );
};

export default App;
