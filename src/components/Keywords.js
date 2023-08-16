import Keyword from './Keyword'

const Keywords = ({keywords, onDelete }) => {
    return (
        <>
            {keywords.map((keyword) => (
                <Keyword key={keyword.id} keyword={keyword} onDelete={onDelete} />
            ))}
        </>
    )
}

export default Keywords