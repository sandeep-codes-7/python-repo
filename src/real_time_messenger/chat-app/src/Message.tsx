function Message(){
    const name = 'sandeep';
    if(name)
        return <h1>hey {name}!</h1>;
    else
        return <h1>Hey world!</h1>
}
export default Message;