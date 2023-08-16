import React from 'react'


function ClearButton(props) {

    return (
        <button className={props.className} onClick={props.onClick}> 
            {props.label}
        </button>
    )
}

export default ClearButton