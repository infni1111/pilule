/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: {
    ignoreDuringBuilds: true, // ignore les erreurs ESLint pendant le build
  },
};

module.exports = nextConfig;
