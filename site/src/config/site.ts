import { SITE_URL } from './site-url.mjs';

/**
 * Facts about the company. Only real, founder-confirmed facts go here.
 * Unknown facts stay null and are marked TODO(founder); schema helpers skip null fields.
 */
export const SITE = {
  name: 'Cybertronix',
  url: SITE_URL,
  city: 'Hyderabad',
  region: 'Telangana',
  country: 'IN',
  // TODO(founder): office street address, postcode and phone (FOUNDER-TODO F1).
  streetAddress: null as string | null,
  postalCode: null as string | null,
  telephone: null as string | null,
  email: null as string | null,
  // TODO(founder): LinkedIn and other official profile URLs.
  sameAs: [] as string[],
  locale: 'en_IN',
};

/** P1–P7 from docs/PAGES.md. Order = nav order. */
export const PAGES = [
  { id: 'P1', label: 'Home', href: '/' },
  { id: 'P2', label: 'Humanoid robots', href: '/humanoid-robots' },
  { id: 'P3', label: 'Robotic arm', href: '/robotic-arm' },
  { id: 'P4', label: 'Cleaning robot', href: '/cleaning-robot' },
  { id: 'P5', label: 'AI vision', href: '/ai-vision' },
  { id: 'P6', label: 'About', href: '/about' },
  { id: 'P7', label: 'Contact', href: '/contact' },
] as const;
