function deleteTrain(machineId) {
    fetch('/delete-train', {
        method: 'POST',
        body: JSON.stringify({ machineId: machineId})
    }).then((_res) => {
        window.location.href = "/trains";
    });
}