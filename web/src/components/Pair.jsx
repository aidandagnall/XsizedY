import React from 'react';
import Choice from '../components/Choice';
import './Pair.css';
import Animals from "../animals.json"

class Pair extends React.Component {

    constructor(props) {
        super(props);

        this.handler = this.handler.bind(this);
    }

    render() {
        this.animalPair = this.GetPair();
        this.number = 2 ** (this.animalPair[1].size - this.animalPair[0].size)
        return (
            <div className='Pair'>
                <div className='Item'>
                    <Choice animals={[this.animalPair[0], this.animalPair[1]]} count ="1" colour="primary" handler={this.handler}/>
                </div>
                <div className='CenterItem'>
                    <h2> or </h2>
                </div>
                <div className='Item'>
                    <Choice animals={[this.animalPair[1], this.animalPair[0]]} counter ={ this.number } colour="danger" handler={this.handler}/>
                </div>
            </div>
        );
    }

    handler() {
        this.forceUpdate();
    }
    
    GetPair() {
        var randX = -1;
        var randY = -1;
        const max = 25;
        var animalX = 0;
        var animalY = 0;
        while (randX === randY || animalX >= animalY) {
            randX = Math.random() * max;
            randY = Math.random() * max;
            animalX = Animals.animals[Math.round(randX)].size
            animalY = Animals.animals[Math.round(randY)].size
        }
        return ([Animals.animals[Math.round(randX)], Animals.animals[Math.round(randY)]]);
    }


}

export default Pair;