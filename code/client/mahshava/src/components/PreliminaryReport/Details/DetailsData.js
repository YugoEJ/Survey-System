import React from "react";
import style from './DetailsData.module.css';
import AccordionDetails from "./AccordionDetails";
import AccordionDetailsB from "./AccordionDetailsB";
import AccordionDetailsC from "./AccordionDetailsC";


export const DetailsData = [
    {
        title: 'מנהיגות ותרבות אירגונית',
        content: <div className={style.Text1}>
                <AccordionDetails/>
            </div>

    },
    {
        title: 'רשתות של מערכות יחסים',
        content: <div className={style.Text2}>
            <AccordionDetailsB/>
        </div>
    },
    {
        title: 'מוכנות להשתנות',
        content: <div className={style.Text3}>
            <AccordionDetailsC/>
        </div>
    }
];