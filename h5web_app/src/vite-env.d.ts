/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_HSDS_URL: string;
  readonly VITE_HSDS_USER: string;
  readonly VITE_HSDS_PASSWORD: string;
  readonly VITE_HSDS_SUBDOMAIN?: string;
  readonly VITE_HSDS_FALLBACK_FILEPATH?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
