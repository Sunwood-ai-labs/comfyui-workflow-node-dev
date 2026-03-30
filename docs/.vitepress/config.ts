import { defineConfig } from "vitepress";

const siteTitle = "ComfyUI Workflow Node Dev";
const siteDescription =
  "Build, refactor, and validate ComfyUI workflows and custom nodes with App mode, schema truth, and runtime evidence.";
const siteOrigin = "https://sunwood-ai-labs.github.io";
const siteBase = "/comfyui-workflow-node-dev/";
const siteUrl = new URL(siteBase, siteOrigin).toString();
const ogImageUrl = new URL("ogp.png", siteUrl).toString();
const repoUrl = "https://github.com/Sunwood-ai-labs/comfyui-workflow-node-dev";

const socialLinks = [
  {
    icon: "github",
    link: repoUrl,
  },
];

const footer = {
  message: "Built for practical ComfyUI workflow and custom-node development.",
  copyright: "Copyright (c) 2026 Sunwood AI Labs",
};

function toPagePath(page: string): string {
  if (page === "index.md") return "/";
  if (page.endsWith("/index.md")) return `/${page.replace(/\/index\.md$/, "")}/`;
  return `/${page.replace(/\.md$/, "")}`;
}

function toAbsoluteUrl(path: string): string {
  return new URL(path.replace(/^\/+/, ""), siteUrl).toString();
}

export default defineConfig({
  title: siteTitle,
  description: siteDescription,
  base: siteBase,
  lang: "en-US",
  cleanUrls: true,
  head: [
    ["link", { rel: "icon", type: "image/svg+xml", href: `${siteBase}favicon.svg` }],
    ["meta", { name: "theme-color", content: "#0F766E" }],
  ],
  sitemap: {
    hostname: siteUrl,
  },
  transformHead({ page, title, description }) {
    const pageUrl = toAbsoluteUrl(toPagePath(page));
    const locale = page.startsWith("ja/") ? "ja_JP" : "en_US";

    return [
      ["link", { rel: "canonical", href: pageUrl }],
      ["meta", { property: "og:type", content: "website" }],
      ["meta", { property: "og:site_name", content: siteTitle }],
      ["meta", { property: "og:locale", content: locale }],
      ["meta", { property: "og:title", content: title }],
      ["meta", { property: "og:description", content: description }],
      ["meta", { property: "og:url", content: pageUrl }],
      ["meta", { property: "og:image", content: ogImageUrl }],
      ["meta", { property: "og:image:type", content: "image/png" }],
      ["meta", { property: "og:image:alt", content: "ComfyUI Workflow Node Dev social card" }],
      ["meta", { name: "twitter:card", content: "summary_large_image" }],
      ["meta", { name: "twitter:title", content: title }],
      ["meta", { name: "twitter:description", content: description }],
      ["meta", { name: "twitter:image", content: ogImageUrl }],
    ];
  },
  locales: {
    root: {
      label: "English",
      lang: "en-US",
      title: siteTitle,
      description: siteDescription,
      themeConfig: {
        logo: "/logo.svg",
        nav: [
          { text: "Home", link: "/" },
          { text: "Getting Started", link: "/guide/getting-started" },
          { text: "Workflow Design", link: "/guide/workflow-design" },
          { text: "App Mode", link: "/guide/app-mode-and-schema" },
          { text: "Validation", link: "/guide/validation-and-ops" },
          { text: "GitHub", link: repoUrl },
        ],
        sidebar: [
          {
            text: "Guide",
            items: [
              { text: "Getting Started", link: "/guide/getting-started" },
              { text: "Workflow Design", link: "/guide/workflow-design" },
              { text: "App Mode and Schema", link: "/guide/app-mode-and-schema" },
              { text: "Validation and Operations", link: "/guide/validation-and-ops" },
            ],
          },
        ],
        socialLinks,
        footer,
      },
    },
    ja: {
      label: "日本語",
      lang: "ja-JP",
      title: siteTitle,
      description:
        "ComfyUI の workflow と custom node を、App mode、schema 真実、runtime 証跡まで含めて整合的に開発するためのドキュメントです。",
      themeConfig: {
        logo: "/logo.svg",
        nav: [
          { text: "ホーム", link: "/ja/" },
          { text: "はじめに", link: "/ja/guide/getting-started" },
          { text: "Workflow 設計", link: "/ja/guide/workflow-design" },
          { text: "App Mode", link: "/ja/guide/app-mode-and-schema" },
          { text: "検証と運用", link: "/ja/guide/validation-and-ops" },
          { text: "GitHub", link: repoUrl },
        ],
        sidebar: [
          {
            text: "ガイド",
            items: [
              { text: "はじめに", link: "/ja/guide/getting-started" },
              { text: "Workflow 設計", link: "/ja/guide/workflow-design" },
              { text: "App Mode と Schema", link: "/ja/guide/app-mode-and-schema" },
              { text: "検証と運用", link: "/ja/guide/validation-and-ops" },
            ],
          },
        ],
        socialLinks,
        footer,
      },
    },
  },
  themeConfig: {
    socialLinks,
    footer,
  },
});
