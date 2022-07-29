import React, {useEffect, useState, useContext} from "react";
import { Context } from "../store/appContext";

export const Profile = () => {
    const {store, actions}= useContext(Context);

    useEffect(()=>{
        actions.privado();

    }, [])

    return <div>
        <h1>{store.permiso? `Acceso a perfil privado concedido ${store.user}`: "404, la página no existe, vuelva a intentarlo."}</h1>


    </div>
}