import { useState } from 'react'
import { Form, Button } from "react-bootstrap";

const ActivateJobForm = ({ onAdd }) => {
  const [method, setMethod] = useState('')
  const [interval, setInterval] = useState('')

  const onSubmit = (e) => {
    e.preventDefault()

    onAdd({ method, interval })

    setMethod('')
    setInterval('')
  }

  return (
    <Form className='activate-form' onSubmit={onSubmit}>
      <Form.Group controlId="formMethod">
        <Form.Label>Method</Form.Label>
        <Form.Control
          as="select"
          custom
          onChange={(e) => setMethod(e.target.value)}
        >
          <option value="0">Choose Method</option>
          <option value="1">MEAN</option>
          <option value="2">MEDIAN</option>
        </Form.Control>
        {/* <Form.Control type="text" placeholder="Enter Method" value={method} onChange={(e) => setMethod(e.target.value)} /> */}
      </Form.Group>

      <Form.Group controlId="formInterval">
        <Form.Label>Interval</Form.Label>
        <Form.Control type="number" placeholder="0" value={interval} onChange={(e) => setInterval(e.target.value)} />
      </Form.Group>

      <Button variant="primary" type="submit" block>
        Activate
      </Button>
    </Form>
  )
}

export default ActivateJobForm
