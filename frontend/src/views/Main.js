import React, { Fragment } from "react";
import {
    Typography,
    Container,
    Grid,
    AppBar,
    Toolbar,
    Button,
} from "@mui/material";
import { Link, NavLink } from "react-router-dom";

const Main = () => {
  return (
     <Fragment>
       <AppBar class="main-app-bar">
         <Toolbar class="main-tool-bar">
           <div class="app-logo">
             App Logo
           </div>
           <div class="app-navlink">
             <NavLink>
               <Button component={Link} to="/covert-word-to-pdf">
                 Word To Pdf
               </Button>
             </NavLink>
           </div>
         </Toolbar>
       </AppBar>
       <div>
         <Grid container>
           <Grid item>
             <div>
               Hello World
             </div>
           </Grid>
         </Grid>
       </div>
     </Fragment>
  );
}


export default Main;
