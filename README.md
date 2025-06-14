# Family Haven - Pregnancy & Parenting Guide AI

**Built during GDG Kolachi Build With AI 2025 Hackathon**

Family Haven is an AI-powered web application designed to provide culturally sensitive pregnancy and parenting guidance for South Asian families, particularly in Pakistan and India. The Minimum Viable Product (MVP) addresses key needs, including doctor-level pregnancy advice, holistic postpartum support, localized child safety tips, mindful parenting, and inclusive resources for fathers, all while respecting cultural taboos.

## Features

- **Culturally Tailored Guidance**: Medical-grade pregnancy and parenting advice customized for South Asian cultural norms, available in English, Urdu, and Hindi.
- **Postpartum & Mental Health Support**: Comprehensive resources for physical recovery and mental health, including anonymous Q&A to destigmatize sensitive topics.
- **Localized Child Safety**: Region-specific abduction prevention strategies and emergency contacts (e.g., 15 in Pakistan, 100 in India).
- **Father-Inclusive Content**: Guidance for fathers to support pregnant partners and engage in childcare, challenging traditional norms.
- **24/7 AI Companion**: Powered by Gemini 2.5, offering empathetic, multilingual responses via a user-friendly chat interface.

## Tech Stack

- **Frontend**: Next.js, Tailwind CSS, Framer Motion
- **Backend**: Next.js API routes for Gemini 2.5 integration
- **Multilingual Support**: i18next for English, Urdu, and Hindi
- **Deployment**: Vercel
- **Other Tools**: Google Generative AI

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Fashad-Ahmed/Family-Heaven.git
   ```
2. Navigate to the project directory:

   ```bash
   cd Family-Heaven
   ```
3. Install dependencies:

   ```bash
   npm install
   ```
4. Set up environment variables:
   - Create a `.env.local` file.
   - Add `GEMINI_API_KEY` (obtain from Google AI Studio).
5. Run the development server:

   ```bash
   npm run dev
   ```
6. Open http://localhost:3000 in your browser.

## Usage

- Access the homepage to interact with the AI chatbot or navigate tabs (Pregnancy, Postpartum, Child Safety, Mindful Parenting).
- Switch between English, Urdu, and Hindi using the language toggle.
- Explore static content for quick tips and emergency contacts.

## Hackathon Context

This MVP was developed during the **GDG Kolachi Build With AI 2025 Hackathon** to address the lack of accessible, culturally relevant parenting resources in South Asia. The app leverages Gemini 2.5 for AI-driven support, Tailwind CSS for responsive design, and Next.js for scalability, creating a prototype that empowers South Asian families.

![image](https://github.com/user-attachments/assets/1cc8256c-1fec-4c5b-b6f2-19c712e2b412)


## Future Enhancements

- Add pregnancy tracking and video consultations for premium tiers.
- Expand partnerships with NGOs and health workers for rural outreach.
- Refine AI prompts based on user feedback to enhance cultural sensitivity.

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License.
