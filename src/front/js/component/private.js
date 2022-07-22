import React, {useEffect, useState, useContext} from "react";
import { Context } from "../store/appContext";

// import { Link } from "react-router-dom";

export const Private = () => {
    // para lograr capturar los datos crearé una variable de estado: 
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const {actions} = useContext(Context);

    // para hacer un console.log cuando las variebles email y password hayan sido modificadas-->hago un useEffect y comprobar que se ha adquirido bien los datos...
    // useEffect(()=>{
    //     console.log(email, password);
    // }, [email, password])
    // de esta manera conseguimos en consola los datos que acabamos de registrar.
    // introducir en el form evento OnSubmit() para rellenar los input
    return <div className="container">
        <form onSubmit={(e)=>{
            e.preventDefault();

        }}
            // para evitar que la página se refresque usamos el preventDde...
            // guardo directamente el valor del email capturado de la siguiente manera: 
            >
            <div className="mb-3">
                <label for="exampleInputEmail1" className="form-label">Email address</label>
                <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" 
                onChange={(e)=>{setEmail(e.target[0].value);

                }}
                />
                <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div className="mb-3">
                <label for="exampleInputPassword1" className="form-label">Password</label>
                <input type="password" className="form-control" id="exampleInputPassword1" />
            </div>
            <div className="mb-3 form-check">
                <input type="password" className="form-check-input" id="exampleCheck1" 
                onChange={(e)=>{setPassword(e.target[1].value);
                }}
                />
                <label className="form-check-label" for="exampleCheck1">Check me out</label>
            </div>
            <button 
            type= "submit"
            className="btn btn-primary"
            onClick={() =>{actions.register(email, password);}}
            >Submit</button>
        </form>
    </div>

}