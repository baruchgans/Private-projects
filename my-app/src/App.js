import React, {useEffect, useState} from 'react';

function MovieList() {
    const [movies, setMovies] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(0);
    const [sortBy, setSortBy] = useState('Title');
    const [sortOrder, setSortOrder] = useState('asc');
    const [inputValue, setInputValue] = useState('');


    useEffect(() => {
        fetch(`https://jsonmock.hackerrank.com/api/movies/search?Title=${searchTerm}&page=${currentPage}`)
            .then(response => response.json())
            .then(data => {
                setMovies(data.data);
                setTotalPages(data.total_pages);
            });
    }, [currentPage, searchTerm, sortBy, sortOrder]);

    const handleSearchSubmit = event => {
        event.preventDefault();
        setSearchTerm(inputValue);
        setCurrentPage(1);
    };

    const handleInputChange = event => {
        setInputValue(event.target.value);
    };

    const handlePageChange = page => {
        setCurrentPage(page);
    };

    const handleSortBy = sortBy => {
        setSortBy(sortBy);
        setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    };

    return (<div>
        <h1>Movies Search</h1>
        <h2>Search for any movie you like:</h2>
        <input type="text"
               placeholder="Search by title"
               id="search-input"
               value={inputValue}
               onChange={handleInputChange}/>
        <button onClick={handleSearchSubmit}>Search</button>
        <button onClick={() => handleSortBy('Title')}>Sort by Title</button>
        <button onClick={() => handleSortBy('Year')}>Sort by Year</button>
        <table>
            <thead>
            <tr>
                <th>MOVIE NAME</th>
                <th>YEAR</th>
            </tr>
            </thead>
            <tbody>
            {movies
                .sort((a, b) => {
                    if (sortBy === "Title") {
                        return sortOrder === 'asc' ? a.Title.localeCompare(b.Title) : b.Title.localeCompare(a.Title);
                    } else {
                        return sortOrder === 'asc' ? a.Year - b.Year : b.Year - a.Year;
                    }
                })
                .map(movie => (<tr key={movie.imdbID}>
                    <td>{movie.Title}</td>
                    <td>{movie.Year}</td>
                </tr>))}
            </tbody>
        </table>
        <Pagination totalPages={totalPages} currentPage={currentPage} onPageChange={handlePageChange}/>
        <div className={'center'}>{totalPages} Total Pages</div>
    </div>);
}

function Pagination({totalPages, currentPage, onPageChange}) {
    const pageWindow = 3;
    const startPage = currentPage - pageWindow < 1 ? 1 : currentPage - pageWindow;
    const endPage = currentPage + pageWindow > totalPages ? totalPages : currentPage + pageWindow;

    return (
        <div className={'center'}>
            {startPage > 1 &&
                <button key="start" onClick={() => onPageChange(1)}>{"<<"}</button>
            }
            {Array.from({length: endPage - startPage + 1}, (_, index) => index + startPage).map(page =>
                <button
                    key={page}
                    onClick={() => onPageChange(page)}
                    disabled={page === currentPage}
                    style={{
                        backgroundColor: page === currentPage ? 'lightblue' : '',
                    }}
                >
                    {page}
                </button>
            )}
            {endPage < totalPages &&
                <button key="end" onClick={() => onPageChange(totalPages)}>{">>"}</button>
            }
        </div>
    );
}


export default MovieList;
