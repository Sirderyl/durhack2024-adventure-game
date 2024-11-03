import { useNavigate } from 'react-router-dom'
import '../App.css'

function Ending() {
 
    const navigate = useNavigate()

    const ending = "With the crown whole in her hands, Lira begins her journey back through the Vale, the mist swirling gently around her as if honoring her silent victory. Each step feels lighter, her heart steadied by a newfound calm. As she follows the winding path, she senses a presence nearby—and then another. \n\n \
        Out of the shadows steps the fox, his golden eyes softened, no longer mocking. He tilts his head, a glint of respect in his gaze. Without a word, he bows his head in acknowledgment and then slips back into the shadows, his form melting into the mist. \n\n \
        A few steps further, Lira hears a soft melody rising from behind the trees. The shy bard emerges, lute in hand, his once uncertain fingers now strumming with confidence. He nods to her, his music swelling with warmth, a silent tribute to her journey. She returns his gaze with a smile, feeling his music carry the unspoken understanding between them. One by one, those she encountered along the way appear—each giving her a look that speaks volumes. Somehow, they all know, even if the rest of the world never will. \n\n \
        When she finally steps beyond the Vale of Shadows, the kingdom lies before her, restored. She makes her way quietly back to the village, watching from a distance as life returns to normal. The streets are alive with laughter and warmth, children running and playing, and villagers celebrating the kingdom’s newfound peace. The crown rests in its rightful place, its purpose fulfilled, its presence the only trace of the journey she undertook. \n\n \
        No one looks her way, no one recognizes her as the one who saved them all. Yet, a gentle peace settles in her chest. She feels no bitterness, no pang of regret—only a quiet pride that swells with each beat of her heart. \n\n \
        For so long, Lira had thought that worth lay in recognition, in the validation of others. But the journey had stripped away her doubts, revealing a truth she now carried within her: Worth is not granted by others; it is claimed in silence, in resilience, in the courage to continue even when no one sees. \n\n \
        She lets the moment settle, breathing in the crisp air, feeling the weight of her own acceptance—a strength no crown could ever give. \n\n \
        As she turns to leave, a single line of the bard’s melody echoes in her mind, and she smiles, knowing that she has not only restored the crown but found her own place, her own value. And with that, Lira disappears down the quiet path leading out of the village, a shadow among the trees, her spirit as whole as the kingdom she saved."


    function handleAdvance() {
        navigate("/the-broken-crown")
    }


  return (
    <>
        <h3 style={{ whiteSpace: 'pre-line' }}>{ending}</h3>
        <button onClick={() => handleAdvance()}>Finish</button>
    </>
  )
}

export default Ending
