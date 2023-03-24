import React, { Fragment } from "react";
import { Grid, Typography, AppBar, Toolbar, Paper, Container} from "@mui/material";
import { Link, NavLink } from "react-router-dom";
import { convertWordToPdf } from "../data/api/documentConverterApi";

const ConvertWordToPdf = () => {
  return (
    <Fragment>
      <AppBar class="convert-word-app-bar">
        <Toolbar class="convert-word-tool-bar">
          <div class="app-logo">App Logo</div>
          <div class="app-nav-link">
            <NavLink>
              <Button component={Link} to=""></Button>
            </NavLink>
          </div>
        </Toolbar>
      </AppBar>
      <div>
        <Typography variant="title" component="div">
          Convert Word To Pdf
        </Typography>
      </div>
    </Fragment>
  );
}
