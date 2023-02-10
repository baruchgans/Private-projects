import React, {useEffect, useState} from 'react';

function MyList() {
    const [var1, setvar1] = useState([]);
    const [var2, setvar2] = useState('');
    const [var3, setvar3] = useState(1);
    const [inputValue, setInputValue] = useState(1);


    function setSomthing(data) {
        setvar3(data.book)
    }

    useEffect(() => {
        fetch(`https://example_url`)
            .then(response => response.json())
            .then(data => {
                setSomthing(data);
            });
    }, [var1, var2, var3]);

        const handleInputChange = event => {
        setInputValue(event.target.value);
        setvar1("blabla")
        setvar2("blabla")
    };




    return (<div>
                <input type="text"
               placeholder="Search something"
               id="search-input"
               value={inputValue}
               onChange={handleInputChange}/>
    </div>);
}




export default MyList;
