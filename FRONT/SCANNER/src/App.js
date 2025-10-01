import React, { useEffect, useState,useRef } from "react";
import {QRCodeCanvas} from 'qrcode.react';
import axios from "axios";


const App = () => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const Ref = useRef(null);
    const [timer, setTimer] = useState("00:00:00");


    const getTimeRemaining = (e) => {
        const total   = Date.parse(e) - Date.parse(new Date());
        const seconds = Math.floor((total / 1000) % 60);
        const minutes = Math.floor(
            (total / 1000 / 60) % 60
        );
        const hours = Math.floor(
            (total / 1000 / 60 / 60) % 24
        );
        return {
            total,
            hours,
            minutes,
            seconds,
        };
    };
    const startTimer = (e) => {
        let { total, hours, minutes, seconds } =
            getTimeRemaining(e);
        if (total >= 0) {
            setTimer(
                (hours > 9 ? hours : "0" + hours) +
                ":" +
                (minutes > 9
                    ? minutes
                    : "0" + minutes) +
                ":" +
                (seconds > 9 ? seconds : "0" + seconds)
            );
        }
        if(total == 0){
          window.open("https://sac.somatto.org.br/connections");
        }
    };   

    const clearTimer = (e) => {

        setTimer("00:00:60");
        if (Ref.current) clearInterval(Ref.current);
        const id = setInterval(() => {
            startTimer(e);
        }, 1000);
        Ref.current = id;
    };

    const getDeadTime = () => {
        let deadline = new Date();
        deadline.setSeconds(deadline.getSeconds() + 60);
        return deadline;
    };

    useEffect(() => {
        clearTimer(getDeadTime());
    }, []);

    useEffect(() => {
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
    const onClickReset = () => {
        clearTimer(getDeadTime());
    };

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;
 return (
        <div className="p-6 max-w-4xl mx-auto" id="BODY">
           <h1 className="text-2xl font-bold mb-4" id="SOMATTO">Financeiro Somatto.org.br</h1>
           <div id="GENERATOR">
           <ul className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
             {data.map(post => (
                 
                 <h2>
                  <h5 className="text-2xl font-bold mb-4" id="SOMATTOQR">
                  {post.qrcode === "Verificado" ? (
                            <span>*Whastapp já esta conectado!</span>
                          ) : (
                            <span>Scaneie o QRCODE abaixo.</span>
                              
                          )}
                  </h5>        
                   

                   <h2  id="SOMATTO"><p id="SOMATTOQR">Redirecionando em:</p>{timer}</h2>
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
                       <button id="GREEN"><span>*Whatsapp Verificado com Sucesso!</span></button>
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
