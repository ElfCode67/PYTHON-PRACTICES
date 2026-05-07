// Simple calculator that sends calculations to Python backend
let display = document.getElementById('display');

function append(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = '';
}

async function calculate() {
    let expression = display.value;
    
    if (expression === '') return;
    
    try {
        // Send to Python backend
        let response = await fetch('http://127.0.0.1:5000/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({expression: expression})
        });
        
        let data = await response.json();
        
        if (data.result !== undefined) {
            display.value = data.result;
        } else {
            display.value = 'Error';
        }
    } catch (error) {
        // If Python backend isn't running, use JavaScript fallback
        try {
            let result = eval(expression);
            display.value = result;
        } catch (e) {
            display.value = 'Error';
        }
    }
}

// Also allow Enter key to calculate
document.getElementById('display').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        calculate();
    }
});