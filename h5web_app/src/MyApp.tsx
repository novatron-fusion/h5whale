import {
  App,
  assertEnvVar,
  buildBasicAuthHeader,
  createBasicFetcher,
  HsdsProvider,
} from '@h5web/app';
import { useMemo } from 'react';

function MyApp() {
  const query = new URLSearchParams(globalThis.location.search);
  const file = query.get('file');
  const URL = import.meta.env.VITE_HSDS_URL;
  const USERNAME = import.meta.env.VITE_HSDS_USER;
  const PASSWORD = import.meta.env.VITE_HSDS_PASSWORD;

  assertEnvVar(URL, 'VITE_HSDS_URL');
  assertEnvVar(USERNAME, 'VITE_HSDS_USER');
  assertEnvVar(PASSWORD, 'VITE_HSDS_PASSWORD');

  

  const fetcher = useMemo(() => {
    return createBasicFetcher({
      headers: buildBasicAuthHeader(USERNAME, PASSWORD),
    });
  }, [USERNAME, PASSWORD]);

  return (
    <HsdsProvider url={URL} filepath={file} fetcher={fetcher}>
      <App />
    </HsdsProvider>
  );
}

export default MyApp;
