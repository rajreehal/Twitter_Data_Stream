import React from 'react'
import * as AiIcons from "react-icons/ai";
import * as IoIcons from "react-icons/io";

export const NavbarData = [
    {
        title: 'Tracker',
        path: '/Tracker',
        icon: <AiIcons.AiFillHome />,
        cName: 'nav-text'
    },
    {
        title: 'Explore',
        path: '/Explore',
        icon: <IoIcons.IoIosPaper/>,
        cName: 'nav-text'
    },
    {
        title: 'Support',
        path: '/Support',
        icon: <IoIcons.IoMdHelpCircle/>,
        cName: 'nav-text'
    }
]
