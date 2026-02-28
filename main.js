
const API = 'http://127.0.0.1:5000'

async function fetchStatus() {
  const r = await fetch(API + '/status')
  const j = await r.json()
  document.getElementById('status').innerText = `Goal: ${j.goal_amount} | Balance: ${j.balance} | Progress: ${j.progress.toFixed(2)}% | Locked: ${j.locked} | Emergency used: ${j.emergency_used}`
}

async function postJson(path, body) {
  const r = await fetch(API + path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  })
  return r.json()
}

document.getElementById('setGoalBtn').addEventListener('click', async () => {
  const amt = parseFloat(document.getElementById('goalAmt').value || 0)
  await postJson('/goal', { amount: amt })
  await fetchStatus()
})

document.getElementById('depositBtn').addEventListener('click', async () => {
  const amt = parseFloat(document.getElementById('depAmt').value || 0)
  await postJson('/deposit', { amount: amt })
  await fetchStatus()
})

document.getElementById('withdrawBtn').addEventListener('click', async () => {
  const r = await postJson('/withdraw', {})
  alert(JSON.stringify(r))
  await fetchStatus()
})

document.getElementById('emergencyBtn').addEventListener('click', async () => {
  const r = await postJson('/emergency_unlock', {})
  alert(JSON.stringify(r))
  await fetchStatus()
})

document.getElementById('predictBtn').addEventListener('click', async () => {
  const r = await fetch(API + '/predict')
  const j = await r.json()
  document.getElementById('prediction').innerText = JSON.stringify(j)
})

fetchStatus()
setInterval(fetchStatus, 5000)
