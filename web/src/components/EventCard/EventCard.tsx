import styles from './EventCard.module.css';
import Image from 'next/image';
import eventPoster from "@/assets/images/Event.jpg";
export default function EventCard() {
    return (
        <a className={`${styles.card} w-full rounded-xl flex flex-row flex-nowrap items-center content-stretch justify-center p-6`}>
            <p className="uppercase not-italic text-xs text-center font-black">Ufc Fight Night: Magomedsharipov vs Magomedsharipov</p>
        </a>
    );
}
