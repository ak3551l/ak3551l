<!DOCTYPE html>
<html lang="en">
    <head>
        <script src="https://unpkg.com/react@17/umd/react.production.min.js" crossorigin></script>
        <script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js" crossorigin></script>
        <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
        <style>
            #app {
                text-align: center;
                font-family: sans-serif;
            }

            #problem {
                font-size: 72px;
            }

            #winner {
                font-size: 72px;
                color: green;
            }

            .incorrect {
                color: red;
            }
        </style>
        <title>Counter</title>
    </head>
    <body>
        <div id="app"></div>

        <script type="text/babel">

            function App() {

                const [state, setState] = React.useState({
                    num1: 1,
                    num2: 1,
                    response: "",
                    score: 0,
                    incorrect: false
                });

                function renderWinScreen() {
                    return (
                        <div id="winner">You won!</div>
                    );
                }

                function inputKeyPress(event) {
                    if (event.key === "Enter") {
                        const answer = parseInt(state.response);
                        if (answer === state.num1 + state.num2) {
                            // User got question right
                            setState({
                                ...state,
                                score: state.score + 1,
                                response: "",
                                num1: Math.ceil(Math.random() * 10),
                                num2: Math.ceil(Math.random() * 10),
                                incorrect: false
                            });
                        } else {
                            // User got question wrong
                            setState({
                                ...state,
                                score: state.score - 1,
                                response: "",
                                incorrect: true
                            })
                        }
                    }
                }

                function updateResponse(event) {
                    setState({
                        ...state,
                        response: event.target.value
                    });
                }

                function renderProblem() {
                    return (
                        <div>
                            <div className={state.incorrect ? "incorrect" : ""} id="problem">
                                {state.num1} + {state.num2}
                            </div>
                            <input onKeyPress={inputKeyPress} onChange={updateResponse} autoFocus={true} value={state.response} />
                            <div>Score: {state.score}</div>
                        </div>
                    )
                }

                if (state.score === 10) {
                    return renderWinScreen();
                } else {
                    return renderProblem();
                }
            }

            ReactDOM.render(<App />, document.querySelector("#app"));
        </script>
    </body>
</html>
