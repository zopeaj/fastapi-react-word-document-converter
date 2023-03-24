import React, { Fragment } from "react";
import { Typography, Button, Grid, Menu, MenuItem, AppBar, Toolbar } from "@mui/material";
import { NavLink, Link } from "react-router-dom";
import { convertCorelDrawToPdf } from "../data/api/documentConverterApi";

const ConvertCorelDrawToPdf = () => {
  return (
     <Fragment>
       <div class="container">
         <AppBar class="document-app-bar">
           <Toolbar class="document-tool-bar">
             <div class="logo">
               App Logo
             </div>
             <div class="nav-link">
               <NavLink>
                 <Button component={Link} to="/">

                 </Button>
               </NavLink>
             </div>
           </Toolbar>
         </AppBar>
       </div>
     </Fragment>
  );
}

export default ConvertCorelDrawToPdf;





