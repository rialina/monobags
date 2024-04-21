// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth', // Smooth scroll to the target
                block: 'start'
            });
        }
    });
});

// Product Click Event (Example for Dynamic Content)
document.querySelectorAll('.product button').forEach(button => {
    button.addEventListener('click', () => {
        const productName = button.parentElement.querySelector('h3').textContent;

        alert(`You have selected the ${productName}.`); // This is a simple alert example.
        
        // Example for more complex functionality, such as opening a modal
        // openProductModal(productName);
    });
});

// Function to open a modal with product details (Example, requires modal structure)
// function openProductModal(productName) {
//     const modal = document.getElementById('productModal');
//     const modalContent = modal.querySelector('.modal-content');
    
//     modalContent.innerHTML = `
//         <h2>Selected Product: ${productName}</h2>
//         <p>Additional details about the product can go here.</p>
//     `;

//     modal.style.display = 'block'; // Show the modal
// }

// Event handling for closing the modal (if implemented)
// window.onclick = function (event) {
//     const modal = document.getElementById('productModal');
//     if (event.target == modal) {
//         modal.style.display = 'none'; // Hide the modal if clicked outside
//     }
// };
