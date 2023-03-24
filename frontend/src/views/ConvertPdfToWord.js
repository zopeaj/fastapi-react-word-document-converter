import React, { Fragment } from "react";
import { Typography, AppBar, Toolbar Button, Grid, List, ListItem, Menu, MenuItem } from "@mui/material";
import { Link, NavLink } from "react-router-dom";
import { convertPdfToWord } from "../data/api/documentConverterApi";

const ConvertPdfToWord = () => {
  return (
    <Fragment>
      <div>
        <AppBar class="convert-pdf-to-word-app-bar">
          <Toolbar class="app-tool-bar">
            <div class="app-logo">App Logo</div>
            <div class="app-nav-link">
              <NavLink>
                <Button component={Link} to=""></Button>
              </NavLink>
            </div>
          </Toolbar>
        </AppBar>
      </div>
    </Fragment>
  );
}

export default ConvertPdfToWord;
