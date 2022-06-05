import React, { useState } from 'react';
import { Details } from './Details';
import styled from 'styled-components';
import { IconContext } from 'react-icons';
import { FiPlus, FiMinus } from 'react-icons/fi';
import LogoPolygon1 from '../../mahshava-admin/LogoHelp/LogoPolygon1'
import LogoPolygon2 from '../../mahshava-admin/LogoHelp/LogoPolygon2'




const Container = styled.div`
  position: absolute;
  top: 10%;
  left: 15%;
`;

const Wrap = styled.div`
  color: #2F3A5F;
  display: flex;
  justify-content: right;
  align-items: center;
  width: 200%;
  text-align: center;
  font-family: 'Heebo';
  font-style: normal;
  font-weight: 600;
  font-size: 6px;
  line-height: 5px;
  text-align: left;
  cursor: pointer;
  h1 {
    padding: 1rem;
    font-family: 'Heebo';
font-style: normal;
font-weight: 300;
font-size: 14px;
line-height: 1px;

color: #333333;
  }
  span {
    margin-right: 0.7 rem;
  }
  
`;
const Dropdown = styled.div`
  width: 100%;
  height: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  float: left;
  p {
    font-size: 1 rem;
    font-family: 'Heebo';
font-style: normal;
text-align: right;
color: #333333;
  }
`;


const AccordionDetails = () => {
    const [clicked, setClicked] = useState(false);

    const toggle = index => {
        if (clicked === index) {
            //if clicked question is already active, then close it
            return setClicked(null);
        }

        setClicked(index);
    };

    return (
            <Container>
                {Details.map((item, index) => {
                    return (
                        <>
                            <Wrap onClick={() => toggle(index)} key={index}>
                                <span>{clicked === index ? <LogoPolygon1 /> : <LogoPolygon2 />}</span>
                                <h1>{item.title}</h1>
                            </Wrap>
                            {clicked === index ? (

                                <Dropdown>

                                <p>{item.content}</p>

                                    </Dropdown>

                                    ) : null}
                        </>
                    );
                })}
            </Container>

    );
};

export default AccordionDetails;