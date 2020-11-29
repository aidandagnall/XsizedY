import React from 'react';
import Button from 'react-bootstrap/Button';
import './Choice.css'

class Choice extends React.Component {

    render() {
        console.log(this.props);
        if (this.props.count === "1"){
            this.number = "A"
            this.name = this.props.animals[0].name
        } else {
            this.number = String(this.props.counter)
            this.name = this.props.animals[0].plural
        }


        return (
            <div>
                <Button variant={this.props.colour} className="Choice" size="lg" onClick={(e) => this.props.handler(this.props.animal)} block>
                    <h1>{this.number} {this.props.animals[1].name} sized {this.name}</h1>
                </Button> {' '}
            </div>
        )
    }
}

export default Choice;