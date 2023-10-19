import {useState} from 'react';
import {Button} from 'primereact/button';
import 'primereact/resources/themes/saga-blue/theme.css';
import 'primereact/resources/primereact.min.css';

function App() {
    const [count,setCount] = useState(0);
    
    return (
        <div className="text-center">
          <h1>Hello?</h1>
            <Button label="Click" onClick={e => setCount(count + 1)}></Button>
            <div className="text-2xl text-900 mt-3">{count}</div>
        </div>
    );
}

export default App;