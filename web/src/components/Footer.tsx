export default function Footer() {
    return (
        <footer className="flex items-center justify-center w-full h-44 text-xs">
            <p>
                &copy; {new Date().getFullYear()} Clover MMA. All rights reserved.
            </p>
        </footer>
    );
}