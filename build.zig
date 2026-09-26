const std = @import("std");

pub fn build(b: *std.Build) void {
    const generate = b.addSystemCommand(&.{ "python3", "scripts/build.py" });

    const site = b.step("site", "Build the static CCAR-P study site");
    site.dependOn(&generate.step);

    b.getInstallStep().dependOn(&generate.step);
}
