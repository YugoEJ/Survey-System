import React, { useEffect } from 'react';
import { Routes } from 'react-router-dom';
import {useLocation, useNavigate} from 'react-router';
import useRouting from '../services/routing/hooks/useRouting';

const BaseLayoutRoutes = () => {
    const navigate = useNavigate();
    const { routes, initialRoute } = useRouting();
    const location = useLocation();


    useEffect(() => {
        if (location.pathname === '/' && routes && routes.length > 0) {
            navigate(initialRoute, { replace: true });
        }
    }, [initialRoute, navigate]);


    return <Routes>{routes}</Routes>;
};

export default BaseLayoutRoutes;
