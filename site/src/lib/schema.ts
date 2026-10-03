import { SITE } from '../config/site';

/** JSON-LD helpers. Each returns a plain object; BaseLayout serialises them into <script type="application/ld+json">. */

type Json = Record<string, unknown>;

const abs = (path: string) => new URL(path, SITE.url).toString();
const orgId = () => abs('/#organization');

/** Drops null/undefined/empty values so unknown facts are never published as placeholders. */
function clean<T extends Json>(obj: T): T {
  return Object.fromEntries(
    Object.entries(obj).filter(([, v]) => v !== null && v !== undefined && !(Array.isArray(v) && v.length === 0)),
  ) as T;
}

function postalAddress(): Json {
  return clean({
    '@type': 'PostalAddress',
    streetAddress: SITE.streetAddress,
    addressLocality: SITE.city,
    addressRegion: SITE.region,
    postalCode: SITE.postalCode,
    addressCountry: SITE.country,
  });
}

export function organization(): Json {
  return clean({
    '@context': 'https://schema.org',
    '@type': 'Organization',
    '@id': orgId(),
    name: SITE.name,
    url: abs('/'),
    email: SITE.email,
    telephone: SITE.telephone,
    address: postalAddress(),
    sameAs: SITE.sameAs,
  });
}

export function localBusiness(): Json {
  return clean({
    '@context': 'https://schema.org',
    '@type': 'LocalBusiness',
    '@id': abs('/#localbusiness'),
    name: SITE.name,
    url: abs('/'),
    parentOrganization: { '@id': orgId() },
    telephone: SITE.telephone,
    email: SITE.email,
    address: postalAddress(),
    areaServed: [
      { '@type': 'City', name: 'Hyderabad' },
      { '@type': 'Country', name: 'India' },
    ],
  });
}

export interface ProductInput {
  name: string;
  description: string;
  path: string;
  image?: string;
  category?: string;
  /** Only real, founder-confirmed specs. */
  additionalProperty?: { name: string; value: string }[];
}

export function product(p: ProductInput): Json {
  return clean({
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: p.name,
    description: p.description,
    url: abs(p.path),
    image: p.image ? abs(p.image) : undefined,
    category: p.category,
    brand: { '@type': 'Brand', name: SITE.name },
    manufacturer: { '@id': orgId() },
    additionalProperty: p.additionalProperty?.map((x) => ({ '@type': 'PropertyValue', ...x })),
  });
}

export function faqPage(items: { q: string; a: string }[]): Json {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: items.map(({ q, a }) => ({
      '@type': 'Question',
      name: q,
      acceptedAnswer: { '@type': 'Answer', text: a },
    })),
  };
}

export function breadcrumbs(trail: { name: string; path: string }[]): Json {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: trail.map((t, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: t.name,
      item: abs(t.path),
    })),
  };
}

export function webPage(title: string, path: string): Json {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebPage',
    name: title,
    url: abs(path),
    isPartOf: { '@id': orgId() },
  };
}
