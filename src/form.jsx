const Form = ({title, q1, q2}) => {

    function checkForm() {
        if (true){
            submitForm()
        }
    }
    function submitForm() {
        print("Hello")
    }

    return (
        <div>
            <h1>{title}</h1>

            <h4>{ q1 }</h4>
            <input type="text" name="a1" />

            <h4>{ q2 }</h4>
            <input type="text" name="a2" />

            <button onClick={ checkForm }>
                Submit
            </button>
        </div>
    )
}

export default Form