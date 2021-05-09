import PropTypes from 'prop-types'
import { Button } from 'react-bootstrap'

const Header = ({ title, onAdd, showForm }) => {
    return (
        <header className='header'>
            <h1>{title}</h1>
            <Button
                variant={showForm ? 'danger' : 'success'}
                onClick={onAdd}
            >{showForm ? 'Close' : 'Activate'}</Button>
        </header>
    )
}

Header.defaultProps = {
    title: 'Lego Exercise'
}

Header.propTypes = {
    title: PropTypes.string
}

export default Header
