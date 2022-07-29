import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
				</Link>
				<div className="ml-auto">
					<Link to="/demo">
						<button className="btn btn-primary">Check the Context in action</button>
					</Link>
				</div>
				<div className="ml-auto ">
					<div className="container">

						<Link to="/register">
							<button className="btn btn-primary">Registrarse</button>
						</Link>
						<Link to="/login">
							<button className="btn btn-primary" style = {{marginLeft: "5px"}}>Iniciar Sesión</button>
						</Link>
					</div>
					
				</div>
			</div>
		</nav>
	);
};
